import { useState, useEffect } from 'react';
import { Button, Form, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import SearchField from '@/components/SearchField';
import CrudModal from '@/components/CrudModal';

export default function SignaturesPage() {
  const { user, token } = useAuth();
  const isAdmin = user?.isAdmin ?? false;

  const [signatures, setSignatures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState(null);

  const emptyForm = { id: '', name: '', description: '' };
  const [form, setForm] = useState(emptyForm);

  const loadSignatures = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch('/signatures', { token });
      setSignatures(Array.isArray(data) ? data : []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadSignatures(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const openCreate = () => {
    setEditing(null);
    setForm(emptyForm);
    setFormError(null);
    setShowModal(true);
  };

  const openEdit = (s) => {
    setEditing(s);
    setForm({ id: s.id, name: s.name, description: s.description ?? '' });
    setFormError(null);
    setShowModal(true);
  };

  const handleDelete = async (id, name) => {
    if (!window.confirm(`¿Eliminar la materia "${name}"?`)) return;
    try {
      await apiFetch(`/signatures/${id}`, { method: 'DELETE', token });
      await loadSignatures();
    } catch (e) {
      alert(`Error: ${e.message}`);
    }
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setSaving(true);
    setFormError(null);

    const payload = {
      name: form.name,
      description: form.description || null,
    };

    try {
      if (editing) {
        await apiFetch(`/signatures/${editing.id}`, { method: 'PUT', token, body: payload });
      } else {
        await apiFetch('/signatures', { method: 'POST', token, body: { id: form.id, ...payload } });
      }
      setShowModal(false);
      await loadSignatures();
    } catch (e) {
      setFormError(e.message);
    } finally {
      setSaving(false);
    }
  };

  const filtered = signatures.filter(s => {
    const q = search.toLowerCase();
    return (
      s.id.toLowerCase().includes(q) ||
      s.name.toLowerCase().includes(q) ||
      (s.description ?? '').toLowerCase().includes(q)
    );
  });

  return (
    <>
      <PageHeader
        title="Materias"
        description={isAdmin ? 'Gestiona las asignaturas disponibles en el sistema.' : 'Consulta de materias. Solo lectura.'}
        action={isAdmin && (
          <Button id="btn-nueva-materia" variant="danger" onClick={openCreate}>
            <span className="material-symbols-outlined me-2" style={{ fontSize: '1rem' }}>add</span>
            Nueva Materia
          </Button>
        )}
      />

      <SearchField
        id="input-buscar-materia"
        className="mb-3"
        placeholder="Buscar por nombre o ID..."
        value={search}
        onChange={e => setSearch(e.target.value)}
      />

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive" footer={`Mostrando ${filtered.length} de ${signatures.length} materias`}>
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Materia</th>
                <th>Descripción</th>
                <th>Estado</th>
                {isAdmin && <th className="text-end">Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {filtered.length === 0 ? (
                <tr><td colSpan={isAdmin ? 5 : 4} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>
                  {search ? 'Sin resultados para la búsqueda' : 'Sin materias registradas'}
                </td></tr>
              ) : (
                filtered.map(s => (
                  <tr key={s.id}>
                    <td><code style={{ color: 'var(--primary-light)' }}>{s.id}</code></td>
                    <td style={{ fontWeight: 600 }}>{s.name}</td>
                    <td style={{ color: 'var(--on-surface-dim)', fontSize: '0.85rem' }}>{s.description ?? '—'}</td>
                    <td>
                      <span className={`badge ${s.is_active ? 'bg-success' : 'bg-secondary'}`}>
                        {s.is_active ? 'Activa' : 'Inactiva'}
                      </span>
                    </td>
                    {isAdmin && (
                      <td className="text-end">
                        <button id={`btn-editar-materia-${s.id}`} className="btn btn-sm btn-outline-secondary me-2" onClick={() => openEdit(s)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>edit</span>
                        </button>
                        <button id={`btn-eliminar-materia-${s.id}`} className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(s.id, s.name)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>delete</span>
                        </button>
                      </td>
                    )}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </SurfacePanel>
      )}

      {isAdmin && (
        <CrudModal
          show={showModal}
          onHide={() => setShowModal(false)}
          title={editing ? 'Editar Materia' : 'Nueva Materia'}
          onSubmit={handleSave}
          error={formError}
          saving={saving}
          submitLabel={editing ? 'Guardar Cambios' : 'Crear Materia'}
          savingLabel="Guardando..."
          submitId="btn-guardar-materia"
        >
          {!editing && (
            <Form.Group className="mb-3">
              <Form.Label>ID de Materia</Form.Label>
              <Form.Control id="input-materia-id" type="text" placeholder="Ej: MAT101" value={form.id} onChange={e => setForm(f => ({ ...f, id: e.target.value }))} required className="bg-dark text-light border-secondary" />
            </Form.Group>
          )}
          <Form.Group className="mb-3">
            <Form.Label>Nombre de la Materia</Form.Label>
            <Form.Control id="input-materia-nombre" type="text" placeholder="Ej: Algebra Lineal" value={form.name} onChange={e => setForm(f => ({ ...f, name: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-1">
            <Form.Label>Descripción <span style={{ color: 'var(--on-surface-dim)' }}>(opcional)</span></Form.Label>
            <Form.Control id="input-materia-desc" as="textarea" rows={2} placeholder="Descripción breve" value={form.description} onChange={e => setForm(f => ({ ...f, description: e.target.value }))} className="bg-dark text-light border-secondary" />
          </Form.Group>
        </CrudModal>
      )}
    </>
  );
}

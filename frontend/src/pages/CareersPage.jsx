import { useState, useEffect } from 'react';
import { Button, Form, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import SearchField from '@/components/SearchField';
import CrudModal from '@/components/CrudModal';

export default function CareersPage() {
  const { user, token } = useAuth();
  const isAdmin = user?.isAdmin ?? false;

  const [careers, setCareers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState(null);

  const emptyForm = { name: '', description: '' };
  const [form, setForm] = useState(emptyForm);

  const loadCareers = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch('/careers', { token });
      setCareers(Array.isArray(data) ? data : []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadCareers(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const openCreate = () => {
    setEditing(null);
    setForm(emptyForm);
    setFormError(null);
    setShowModal(true);
  };

  const openEdit = (c) => {
    setEditing(c);
    setForm({ name: c.name, description: c.description ?? '' });
    setFormError(null);
    setShowModal(true);
  };

  const handleDeactivate = async (id, name) => {
    if (!window.confirm(`¿Desactivar la carrera "${name}"?`)) return;
    try {
      await apiFetch(`/careers/${id}`, { method: 'DELETE', token });
      await loadCareers();
    } catch (e) {
      alert(`Error: ${e.message}`);
    }
  };

  const handleReactivate = async (id) => {
    try {
      await apiFetch(`/careers/${id}/reactivate`, { method: 'POST', token });
      await loadCareers();
    } catch (e) {
      alert(`Error: ${e.message}`);
    }
  };

  const handleDestroy = async (id, name) => {
    if (!window.confirm(`⚠️ ¿Eliminar DEFINITIVAMENTE la carrera "${name}"? Esta acción no se puede deshacer.`)) return;
    try {
      await apiFetch(`/careers/${id}/destroy`, { method: 'DELETE', token });
      await loadCareers();
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
        await apiFetch(`/careers/${editing.id}`, { method: 'PUT', token, body: payload });
      } else {
        await apiFetch('/careers', { method: 'POST', token, body: payload });
      }
      setShowModal(false);
      await loadCareers();
    } catch (e) {
      setFormError(e.message);
    } finally {
      setSaving(false);
    }
  };

  const filtered = careers.filter(c => {
    const q = search.toLowerCase();
    return (
      `${c.id}`.toLowerCase().includes(q) ||
      c.name.toLowerCase().includes(q) ||
      (c.description ?? '').toLowerCase().includes(q)
    );
  });

  return (
    <>
      <PageHeader
        title="Carreras"
        description={isAdmin ? 'Administra las carreras activas e históricas.' : 'Consulta de carreras. Solo lectura.'}
        action={isAdmin && (
          <Button id="btn-nueva-carrera" variant="danger" onClick={openCreate}>
            <span className="material-symbols-outlined me-2" style={{ fontSize: '1rem' }}>add</span>
            Nueva Carrera
          </Button>
        )}
      />

      <SearchField
        id="input-buscar-carrera"
        className="mb-3"
        placeholder="Buscar por nombre o ID..."
        value={search}
        onChange={e => setSearch(e.target.value)}
      />

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive" footer={`Mostrando ${filtered.length} de ${careers.length} carreras`}>
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Carrera</th>
                <th>Descripción</th>
                <th>Estado</th>
                {isAdmin && <th className="text-end">Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {filtered.length === 0 ? (
                <tr><td colSpan={isAdmin ? 5 : 4} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>
                  {search ? 'Sin resultados para la búsqueda' : 'Sin carreras registradas'}
                </td></tr>
              ) : (
                filtered.map(c => (
                  <tr key={c.id}>
                    <td style={{ color: 'var(--on-surface-dim)' }}>{c.id}</td>
                    <td style={{ fontWeight: 600 }}>{c.name}</td>
                    <td style={{ color: 'var(--on-surface-dim)', fontSize: '0.85rem' }}>{c.description ?? '—'}</td>
                    <td>
                      <span className={`badge ${c.is_active ? 'bg-success' : 'bg-secondary'}`}>
                        {c.is_active ? 'Activa' : 'Inactiva'}
                      </span>
                    </td>
                    {isAdmin && (
                      <td className="text-end">
                        <button id={`btn-editar-carrera-${c.id}`} className="btn btn-sm btn-outline-secondary me-1" onClick={() => openEdit(c)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>edit</span>
                        </button>
                        {c.is_active ? (
                          <button id={`btn-desactivar-carrera-${c.id}`} className="btn btn-sm btn-outline-warning me-1" onClick={() => handleDeactivate(c.id, c.name)}>
                            <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>pause_circle</span>
                          </button>
                        ) : (
                          <button id={`btn-reactivar-carrera-${c.id}`} className="btn btn-sm btn-outline-success me-1" onClick={() => handleReactivate(c.id)}>
                            <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>play_circle</span>
                          </button>
                        )}
                        <button id={`btn-eliminar-carrera-${c.id}`} className="btn btn-sm btn-outline-danger" onClick={() => handleDestroy(c.id, c.name)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>delete_forever</span>
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
          title={editing ? 'Editar Carrera' : 'Nueva Carrera'}
          onSubmit={handleSave}
          error={formError}
          saving={saving}
          submitLabel={editing ? 'Guardar Cambios' : 'Crear Carrera'}
          savingLabel="Guardando..."
          submitId="btn-guardar-carrera"
        >
          <Form.Group className="mb-3">
            <Form.Label>Nombre de la Carrera</Form.Label>
            <Form.Control id="input-carrera-nombre" type="text" placeholder="Ej: Ingeniería en Software" value={form.name} onChange={e => setForm(f => ({ ...f, name: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-1">
            <Form.Label>Descripción <span style={{ color: 'var(--on-surface-dim)' }}>(opcional)</span></Form.Label>
            <Form.Control id="input-carrera-desc" as="textarea" rows={2} placeholder="Descripción breve" value={form.description} onChange={e => setForm(f => ({ ...f, description: e.target.value }))} className="bg-dark text-light border-secondary" />
          </Form.Group>
        </CrudModal>
      )}
    </>
  );
}

import { useState, useEffect } from 'react';
import { Button, Form, Spinner, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import SearchField from '@/components/SearchField';
import CrudModal from '@/components/CrudModal';

export default function StudentsPage() {
  const { user, token } = useAuth();
  const isAdmin = user?.isAdmin ?? false;

  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState(null);

  const emptyForm = { id: '', first_name: '', last_name: '', nickname: '', email: '', career_id: '', is_active: true };
  const [form, setForm] = useState(emptyForm);

  const loadStudents = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch('/students', { token });
      setStudents(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadStudents(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const openCreate = () => {
    setEditing(null);
    setForm(emptyForm);
    setFormError(null);
    setShowModal(true);
  };

  const openEdit = (s) => {
    setEditing(s);
    setForm({ id: s.id, first_name: s.first_name, last_name: s.last_name, nickname: s.nickname ?? '', email: s.email, career_id: s.career_id ?? '', is_active: s.is_active });
    setFormError(null);
    setShowModal(true);
  };

  const handleDelete = async (id, name) => {
    if (!window.confirm(`¿Eliminar al estudiante "${name}"?`)) return;
    try {
      await apiFetch(`/students/${id}`, { method: 'DELETE', token });
      await loadStudents();
    } catch (e) {
      alert(`Error: ${e.message}`);
    }
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setSaving(true);
    setFormError(null);
    try {
      if (editing) {
        await apiFetch(`/students/${editing.id}`, { method: 'PUT', token, body: { first_name: form.first_name, last_name: form.last_name, nickname: form.nickname || null, email: form.email, career_id: form.career_id || null, is_active: form.is_active } });
      } else {
        await apiFetch('/students', { method: 'POST', token, body: form });
      }
      setShowModal(false);
      await loadStudents();
    } catch (e) {
      setFormError(e.message);
    } finally {
      setSaving(false);
    }
  };

  // Filtrado local por nombre, apodo o ID
  const filtered = students.filter(s => {
    const q = search.toLowerCase();
    return (
      s.id.toLowerCase().includes(q) ||
      s.first_name.toLowerCase().includes(q) ||
      s.last_name.toLowerCase().includes(q) ||
      (s.nickname ?? '').toLowerCase().includes(q) ||
      s.email.toLowerCase().includes(q)
    );
  });

  return (
    <>
      <PageHeader
        title="Expedientes de Estudiantes"
        description={isAdmin ? 'Gestión completa de alumnos inscritos.' : 'Consulta de alumnos. Solo lectura.'}
        action={isAdmin && (
          <Button id="btn-nuevo-estudiante" variant="danger" onClick={openCreate}>
            <span className="material-symbols-outlined me-2" style={{ fontSize: '1rem' }}>person_add</span>
            Nuevo Estudiante
          </Button>
        )}
      />

      <SearchField
        id="input-buscar-estudiante"
        className="mb-3"
        placeholder="Buscar por nombre, ID o correo..."
        value={search}
        onChange={e => setSearch(e.target.value)}
      />

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive" footer={`Mostrando ${filtered.length} de ${students.length} expedientes`}>
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Apodo</th>
                <th>Nombre Completo</th>
                <th>Correo Electrónico</th>
                <th>Estado</th>
                {isAdmin && <th className="text-end">Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {filtered.length === 0 ? (
                <tr><td colSpan={isAdmin ? 6 : 5} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>
                  {search ? 'Sin resultados para la búsqueda' : 'Sin estudiantes registrados'}
                </td></tr>
              ) : (
                filtered.map(s => (
                  <tr key={s.id}>
                    <td><code style={{ color: 'var(--primary-light)' }}>{s.id}</code></td>
                    <td style={{ fontWeight: 600 }}>{s.nickname ?? '—'}</td>
                    <td style={{ fontWeight: 600 }}>{s.first_name} {s.last_name}</td>
                    <td style={{ fontSize: '0.85rem' }}>{s.email}</td>
                    <td>
                      <span className={`badge ${s.is_active ? 'bg-success' : 'bg-secondary'}`}>
                        {s.is_active ? 'Activo' : 'Inactivo'}
                      </span>
                    </td>
                    {isAdmin && (
                      <td className="text-end">
                        <button id={`btn-editar-est-${s.id}`} className="btn btn-sm btn-outline-secondary me-2" onClick={() => openEdit(s)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>edit</span>
                        </button>
                        <button id={`btn-eliminar-est-${s.id}`} className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(s.id, `${s.first_name} ${s.last_name}`)}>
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
          title={editing ? 'Editar Estudiante' : 'Nuevo Estudiante'}
          onSubmit={handleSave}
          error={formError}
          saving={saving}
          submitLabel={editing ? 'Guardar Cambios' : 'Crear Estudiante'}
          savingLabel="Guardando..."
          submitId="btn-guardar-est"
        >
          {!editing && (
            <Form.Group className="mb-3">
              <Form.Label>ID de Matrícula</Form.Label>
              <Form.Control id="input-est-id" type="text" placeholder="Ej: EST001" value={form.id} onChange={e => setForm(f => ({ ...f, id: e.target.value }))} required className="bg-dark text-light border-secondary" />
            </Form.Group>
          )}
          <div className="row g-2 mb-3">
            <div className="col-6">
              <Form.Label>Nombre(s)</Form.Label>
              <Form.Control id="input-est-nombre" type="text" placeholder="Nombre" value={form.first_name} onChange={e => setForm(f => ({ ...f, first_name: e.target.value }))} required className="bg-dark text-light border-secondary" />
            </div>
            <div className="col-6">
              <Form.Label>Apellidos</Form.Label>
              <Form.Control id="input-est-apellido" type="text" placeholder="Apellidos" value={form.last_name} onChange={e => setForm(f => ({ ...f, last_name: e.target.value }))} required className="bg-dark text-light border-secondary" />
            </div>
          </div>
          <Form.Group className="mb-3">
            <Form.Label>Apodo / Nick <span style={{ color: 'var(--on-surface-dim)' }}>(opcional)</span></Form.Label>
            <Form.Control id="input-est-apodo" type="text" placeholder="Apodo" value={form.nickname} onChange={e => setForm(f => ({ ...f, nickname: e.target.value }))} className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Correo Electrónico</Form.Label>
            <Form.Control id="input-est-email" type="email" placeholder="correo@ubbj.edu.mx" value={form.email} onChange={e => setForm(f => ({ ...f, email: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          {editing && (
            <Form.Check id="check-est-activo" className="mt-2" type="switch" label="Estudiante activo" checked={form.is_active} onChange={e => setForm(f => ({ ...f, is_active: e.target.checked }))} />
          )}
        </CrudModal>
      )}
    </>
  );
}

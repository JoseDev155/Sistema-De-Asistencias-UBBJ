import { useState, useEffect } from 'react';
import { Button, Form, Spinner, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import CrudModal from '@/components/CrudModal';

export default function EnrollmentsPage() {
  const { user, token } = useAuth();
  const isAdmin = user?.isAdmin ?? false;

  const [enrollments, setEnrollments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [saving, setSaving] = useState(false);
  const [formError, setFormError] = useState(null);

  const emptyForm = { enrollment_date: '', student_id: '', group_id: '' };
  const [form, setForm] = useState(emptyForm);

  const loadEnrollments = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch('/enrollments', { token });
      setEnrollments(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadEnrollments(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const openCreate = () => {
    setEditing(null);
    setForm(emptyForm);
    setFormError(null);
    setShowModal(true);
  };

  const openEdit = (en) => {
    setEditing(en);
    setForm({ enrollment_date: en.enrollment_date, student_id: en.student_id, group_id: en.group_id });
    setFormError(null);
    setShowModal(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm(`¿Eliminar la inscripción #${id}?`)) return;
    try {
      await apiFetch(`/enrollments/${id}`, { method: 'DELETE', token });
      await loadEnrollments();
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
        await apiFetch(`/enrollments/${editing.id}`, { method: 'PUT', token, body: form });
      } else {
        await apiFetch('/enrollments', { method: 'POST', token, body: form });
      }
      setShowModal(false);
      await loadEnrollments();
    } catch (e) {
      setFormError(e.message);
    } finally {
      setSaving(false);
    }
  };

  return (
    <>
      <PageHeader
        title="Inscripciones"
        description={isAdmin ? 'Administra las inscripciones de alumnos a grupos.' : 'Inscripciones de alumnos. Solo lectura.'}
        action={isAdmin && (
          <Button id="btn-nueva-inscripcion" variant="danger" onClick={openCreate}>
            <span className="material-symbols-outlined me-2" style={{ fontSize: '1rem' }}>add</span>
            Nueva Inscripción
          </Button>
        )}
      />

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive" footer={`${enrollments.length} inscripciones`}>
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Estudiante (ID)</th>
                <th>Grupo (ID)</th>
                <th>Fecha de Inscripción</th>
                {isAdmin && <th className="text-end">Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {enrollments.length === 0 ? (
                <tr><td colSpan={isAdmin ? 5 : 4} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>Sin inscripciones registradas</td></tr>
              ) : (
                enrollments.map(en => (
                  <tr key={en.id}>
                    <td style={{ color: 'var(--on-surface-dim)' }}>{en.id}</td>
                    <td><code style={{ color: 'var(--primary-light)' }}>{en.student_id}</code></td>
                    <td><code style={{ color: 'var(--primary-light)' }}>{en.group_id}</code></td>
                    <td style={{ fontSize: '0.85rem', color: 'var(--on-surface-dim)' }}>{en.enrollment_date}</td>
                    {isAdmin && (
                      <td className="text-end">
                        <button id={`btn-editar-insc-${en.id}`} className="btn btn-sm btn-outline-secondary me-2" onClick={() => openEdit(en)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>edit</span>
                        </button>
                        <button id={`btn-eliminar-insc-${en.id}`} className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(en.id)}>
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
          title={editing ? 'Editar Inscripción' : 'Nueva Inscripción'}
          onSubmit={handleSave}
          error={formError}
          saving={saving}
          submitLabel={editing ? 'Guardar Cambios' : 'Inscribir'}
          savingLabel="Guardando..."
          submitId="btn-guardar-insc"
        >
          <Form.Group className="mb-3">
            <Form.Label>ID del Estudiante</Form.Label>
            <Form.Control id="input-insc-estudiante" type="text" placeholder="Ej: EST001" value={form.student_id} onChange={e => setForm(f => ({ ...f, student_id: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>ID del Grupo</Form.Label>
            <Form.Control id="input-insc-grupo" type="text" placeholder="Ej: GRP001" value={form.group_id} onChange={e => setForm(f => ({ ...f, group_id: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-1">
            <Form.Label>Fecha de Inscripción</Form.Label>
            <Form.Control id="input-insc-fecha" type="date" value={form.enrollment_date} onChange={e => setForm(f => ({ ...f, enrollment_date: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
        </CrudModal>
      )}
    </>
  );
}

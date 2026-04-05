import { useState, useEffect } from 'react';
import { Button, Form, Spinner, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import CrudModal from '@/components/CrudModal';

export default function GroupsPage() {
  const { user, token } = useAuth();
  const isAdmin = user?.isAdmin ?? false;

  const [groups, setGroups]       = useState([]);
  const [loading, setLoading]     = useState(true);
  const [error, setError]         = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing]     = useState(null); // null = crear | objeto = editar
  const [saving, setSaving]       = useState(false);
  const [formError, setFormError] = useState(null);

  const emptyForm = { id: '', name: '', description: '', user_id: '' };
  const [form, setForm] = useState(emptyForm);

  // ── Carga de grupos ──────────────────────────────────────────
  const loadGroups = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch('/groups', { token });
      setGroups(data);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { loadGroups(); }, []); // eslint-disable-line react-hooks/exhaustive-deps

  // ── Handlers modal ───────────────────────────────────────────
  const openCreate = () => {
    setEditing(null);
    setForm(emptyForm);
    setFormError(null);
    setShowModal(true);
  };

  const openEdit = (g) => {
    setEditing(g);
    setForm({ id: g.id, name: g.name, description: g.description ?? '', user_id: g.user_id ?? '' });
    setFormError(null);
    setShowModal(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm(`¿Eliminar el grupo "${id}"? Esta acción no se puede deshacer.`)) return;
    try {
      await apiFetch(`/groups/${id}`, { method: 'DELETE', token });
      await loadGroups();
    } catch (e) {
      alert(`Error al eliminar: ${e.message}`);
    }
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setSaving(true);
    setFormError(null);
    try {
      if (editing) {
        await apiFetch(`/groups/${editing.id}`, {
          method: 'PUT',
          token,
          body: { name: form.name, description: form.description, user_id: form.user_id || null },
        });
      } else {
        await apiFetch('/groups', {
          method: 'POST',
          token,
          body: form,
        });
      }
      setShowModal(false);
      await loadGroups();
    } catch (e) {
      setFormError(e.message);
    } finally {
      setSaving(false);
    }
  };

  // ── Render ───────────────────────────────────────────────────
  return (
    <>
      <PageHeader
        title={isAdmin ? 'Gestión de Grupos' : 'Mis Grupos'}
        description={isAdmin ? 'Crea y administra los grupos académicos asignados a profesores.' : 'Grupos en los que impartes clase. Solo lectura.'}
        action={isAdmin && (
          <Button id="btn-nuevo-grupo" variant="danger" onClick={openCreate}>
            <span className="material-symbols-outlined me-2" style={{ fontSize: '1rem' }}>add</span>
            Nuevo Grupo
          </Button>
        )}
      />

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive">
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre del Grupo</th>
                <th>Descripción</th>
                <th>Profesor (ID)</th>
                {isAdmin && <th className="text-end">Acciones</th>}
              </tr>
            </thead>
            <tbody>
              {groups.length === 0 ? (
                <tr><td colSpan={isAdmin ? 5 : 4} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>Sin grupos registrados</td></tr>
              ) : (
                groups.map(g => (
                  <tr key={g.id}>
                    <td><code style={{ color: 'var(--primary-light)' }}>{g.id}</code></td>
                    <td style={{ fontWeight: 600 }}>{g.name}</td>
                    <td style={{ color: 'var(--on-surface-dim)', fontSize: '0.85rem' }}>{g.description ?? '—'}</td>
                    <td style={{ fontSize: '0.85rem' }}>{g.user_id ?? '—'}</td>
                    {isAdmin && (
                      <td className="text-end">
                        <button id={`btn-editar-${g.id}`} className="btn btn-sm btn-outline-secondary me-2" onClick={() => openEdit(g)}>
                          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>edit</span>
                        </button>
                        <button id={`btn-eliminar-${g.id}`} className="btn btn-sm btn-outline-danger" onClick={() => handleDelete(g.id)}>
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
          title={editing ? 'Editar Grupo' : 'Nuevo Grupo'}
          onSubmit={handleSave}
          error={formError}
          saving={saving}
          submitLabel={editing ? 'Guardar Cambios' : 'Crear Grupo'}
          savingLabel="Guardando..."
          submitId="btn-guardar-grupo"
        >
          {!editing && (
            <Form.Group className="mb-3">
              <Form.Label>ID del Grupo</Form.Label>
              <Form.Control id="input-grupo-id" type="text" placeholder="Ej: GRP008" value={form.id} onChange={e => setForm(f => ({ ...f, id: e.target.value }))} required className="bg-dark text-light border-secondary" />
            </Form.Group>
          )}
          <Form.Group className="mb-3">
            <Form.Label>Nombre del Grupo</Form.Label>
            <Form.Control id="input-grupo-nombre" type="text" placeholder="Ej: Matemáticas I — Turno Matutino" value={form.name} onChange={e => setForm(f => ({ ...f, name: e.target.value }))} required className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Descripción <span style={{ color: 'var(--on-surface-dim)' }}>(opcional)</span></Form.Label>
            <Form.Control id="input-grupo-desc" as="textarea" rows={2} placeholder="Descripción breve del grupo" value={form.description} onChange={e => setForm(f => ({ ...f, description: e.target.value }))} className="bg-dark text-light border-secondary" />
          </Form.Group>
          <Form.Group className="mb-1">
            <Form.Label>ID del Profesor Asignado <span style={{ color: 'var(--on-surface-dim)' }}>(opcional)</span></Form.Label>
            <Form.Control id="input-grupo-profesor" type="text" placeholder="Ej: PROF001" value={form.user_id} onChange={e => setForm(f => ({ ...f, user_id: e.target.value }))} className="bg-dark text-light border-secondary" />
          </Form.Group>
        </CrudModal>
      )}
    </>
  );
}

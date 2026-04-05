import { useState, useEffect } from 'react';
import { Button, Alert } from 'react-bootstrap';
import { useAuth } from '@/context/AuthContext';
import { apiFetch } from '@/api/apiClient';
import PageHeader from '@/components/PageHeader';
import LoadingState from '@/components/LoadingState';
import SurfacePanel from '@/components/SurfacePanel';
import SearchField from '@/components/SearchField';

const STATUS_LABELS = { PRESENT: 'Presente', ABSENT: 'Ausente', LATE: 'Retardo', JUSTIFIED: 'Justificado', LEFT_EARLY: 'Salió Temprano' };
const STATUS_BADGE = { PRESENT: 'bg-success', ABSENT: 'bg-danger', LATE: 'bg-warning text-dark', JUSTIFIED: 'bg-info text-dark', LEFT_EARLY: 'bg-secondary' };

export default function AttendancePage() {
  const { token } = useAuth();
  const [attendances, setAttendances] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [groupId, setGroupId] = useState('GRP001');
  const [groupInput, setGroupInput] = useState('GRP001');

  const load = async (gid) => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiFetch(`/attendances/group/${gid}/calculated-with-nickname`, { token });
      setAttendances(Array.isArray(data) ? data : []);
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { load(groupId); }, [groupId]); // eslint-disable-line react-hooks/exhaustive-deps

  const handleFilter = (e) => {
    e.preventDefault();
    const trimmed = groupInput.trim().toUpperCase();
    if (trimmed) setGroupId(trimmed);
  };

  return (
    <>
      <PageHeader
        title="Registros de Asistencia"
        description="Consulta los registros de llegada por grupo."
      />

      <form className="mb-3 d-flex gap-2 align-items-center" onSubmit={handleFilter} style={{ maxWidth: 360 }}>
        <SearchField
          id="input-filtro-grupo"
          icon="groups"
          placeholder="ID del grupo (Ej: GRP001)"
          value={groupInput}
          onChange={e => setGroupInput(e.target.value)}
          className="mb-0"
        />
        <Button id="btn-filtrar-grupo" type="submit" variant="danger" className="text-nowrap">
          Filtrar
        </Button>
      </form>

      {loading && <LoadingState />}
      {error && <Alert variant="danger">{error}</Alert>}

      {!loading && !error && (
        <SurfacePanel className="table-responsive" footer={`${attendances.length} registros · Grupo ${groupId}`}>
          <table className="table table-dark table-hover mb-0 crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Apodo</th>
                <th>Fecha</th>
                <th>Hora de Llegada</th>
                <th>Estado Calculado</th>
                <th>Notas</th>
              </tr>
            </thead>
            <tbody>
              {attendances.length === 0 ? (
                <tr><td colSpan={6} className="text-center py-5" style={{ color: 'var(--on-surface-dim)' }}>Sin registros para el grupo <strong>{groupId}</strong></td></tr>
              ) : (
                attendances.map(a => (
                  <tr key={a.id}>
                    <td style={{ color: 'var(--on-surface-dim)' }}>{a.id}</td>
                    <td style={{ fontWeight: 600 }}>{a.nickname ?? '—'}</td>
                    <td style={{ fontSize: '0.85rem' }}>{a.attendance_date}</td>
                    <td style={{ fontWeight: 600 }}>{a.arrival_time ?? <span style={{ color: 'var(--on-surface-dim)' }}>—</span>}</td>
                    <td>
                      {a.status ? (
                        <span className={`badge ${STATUS_BADGE[a.status] ?? 'bg-secondary'}`}>
                          {STATUS_LABELS[a.status] ?? a.status}
                        </span>
                      ) : (
                        <span className="badge bg-secondary">Sin horario</span>
                      )}
                    </td>
                    <td style={{ fontSize: '0.8rem', color: 'var(--on-surface-dim)' }}>{a.notes ?? '—'}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </SurfacePanel>
      )}
    </>
  );
}

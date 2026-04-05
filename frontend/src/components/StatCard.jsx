export default function StatCard({ label, value, icon, color = 'var(--on-surface)' }) {
  return (
    <div style={{ background: 'var(--surface-raised)', border: '1px solid var(--border)', borderRadius: 8, padding: '1rem' }}>
      <div className="d-flex align-items-center gap-2 mb-1">
        <span className="material-symbols-outlined" style={{ fontSize: '1.1rem', color }}>{icon}</span>
        <span style={{ fontSize: '0.72rem', fontWeight: 700, letterSpacing: '1px', textTransform: 'uppercase', color: 'var(--on-surface-dim)' }}>
          {label}
        </span>
      </div>
      <div style={{ fontSize: '2rem', fontWeight: 700, fontFamily: 'Instrument Sans, sans-serif', color }}>{value}</div>
    </div>
  );
}
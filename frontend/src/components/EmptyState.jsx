export default function EmptyState({ icon = 'info', title, message, minHeight = 240 }) {
  return (
    <div
      className="d-flex align-items-center justify-content-center"
      style={{
        minHeight,
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: 10,
        color: 'var(--on-surface-dim)',
      }}
    >
      <div className="text-center px-3">
        <span className="material-symbols-outlined d-block mb-2" style={{ fontSize: '2.5rem' }}>{icon}</span>
        {title && <h6 className="headline mb-2" style={{ fontWeight: 700 }}>{title}</h6>}
        <p className="mb-0" style={{ fontSize: '0.9rem' }}>{message}</p>
      </div>
    </div>
  );
}
export default function SurfacePanel({ children, className = '', style = {}, footer }) {
  return (
    <div
      className={className}
      style={{
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: 10,
        ...style,
      }}
    >
      {children}
      {footer && (
        <div className="px-3 py-2" style={{ color: 'var(--on-surface-dim)', fontSize: '0.8rem' }}>
          {footer}
        </div>
      )}
    </div>
  );
}
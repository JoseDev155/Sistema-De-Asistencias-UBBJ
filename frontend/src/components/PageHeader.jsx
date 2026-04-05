import { Link } from 'react-router-dom';

export default function PageHeader({
  title,
  description,
  action,
  backTo = '/dashboard',
  backLabel = 'Inicio',
}) {
  return (
    <div className="page-header">
      <div>
        <Link to={backTo} className="page-header-back">
          <span className="material-symbols-outlined" style={{ fontSize: '0.9rem' }}>arrow_back</span>
          {backLabel}
        </Link>
        <h1 className="headline mb-0" style={{ fontSize: '1.6rem', fontWeight: 700 }}>{title}</h1>
        {description && (
          <p style={{ color: 'var(--on-surface-dim)', fontSize: '0.85rem', marginBottom: 0 }}>
            {description}
          </p>
        )}
      </div>
      {action}
    </div>
  );
}
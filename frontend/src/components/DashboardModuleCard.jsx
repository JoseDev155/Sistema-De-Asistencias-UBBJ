import { Link } from 'react-router-dom';

export default function DashboardModuleCard({ path, icon, title, desc, compact = false }) {
  return (
    <Link to={path} className={`module-card${compact ? ' module-card-compact' : ''}`}>
      <div className={`module-card-icon${compact ? ' module-card-icon-compact' : ''}`}>
        <span className="material-symbols-outlined">{icon}</span>
      </div>
      <div className={`module-card-title${compact ? ' module-card-title-compact' : ''}`}>{title}</div>
      <div className={`module-card-desc${compact ? ' module-card-desc-compact' : ''}`}>{desc}</div>
    </Link>
  );
}
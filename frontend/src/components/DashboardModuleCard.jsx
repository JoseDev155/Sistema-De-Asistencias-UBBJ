import { Link } from 'react-router-dom';

export default function DashboardModuleCard({ path, icon, title, desc }) {
  return (
    <Link to={path} className="module-card">
      <div className="module-card-icon">
        <span className="material-symbols-outlined">{icon}</span>
      </div>
      <div className="module-card-title">{title}</div>
      <div className="module-card-desc">{desc}</div>
    </Link>
  );
}
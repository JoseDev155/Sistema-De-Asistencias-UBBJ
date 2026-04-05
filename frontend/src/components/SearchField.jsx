export default function SearchField({
  id,
  value,
  onChange,
  placeholder,
  icon = 'search',
  className = '',
  type = 'text',
}) {
  return (
    <div className={className} style={{ maxWidth: 360 }}>
      <div className="input-group">
        <span className="input-group-text bg-dark border-secondary text-secondary">
          <span className="material-symbols-outlined" style={{ fontSize: '1.1rem' }}>{icon}</span>
        </span>
        <input
          id={id}
          type={type}
          className="form-control bg-dark text-light border-secondary"
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />
      </div>
    </div>
  );
}
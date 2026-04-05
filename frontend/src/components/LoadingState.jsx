import { Spinner } from 'react-bootstrap';

export default function LoadingState({ variant = 'danger', label, className = 'py-5' }) {
  return (
    <div className={`text-center ${className}`}>
      <Spinner animation="border" variant={variant} />
      {label && <div className="mt-3 text-secondary">{label}</div>}
    </div>
  );
}
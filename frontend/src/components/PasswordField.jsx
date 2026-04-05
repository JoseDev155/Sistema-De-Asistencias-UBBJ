import { useState } from 'react';
import { Form } from 'react-bootstrap';

export default function PasswordField({
  id,
  label,
  value,
  onChange,
  placeholder = '••••••••••••',
  required = true,
}) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <Form.Group className="mb-4">
      <Form.Label className="text-secondary text-uppercase fw-bold" style={{ fontSize: '0.8rem', letterSpacing: '1px' }}>
        {label}
      </Form.Label>
      <div className="position-relative">
        <Form.Control
          id={id}
          type={showPassword ? 'text' : 'password'}
          placeholder={placeholder}
          className="bg-dark text-light border-secondary p-3 pe-5"
          value={value}
          onChange={onChange}
          required={required}
          style={{ paddingRight: '3rem' }}
        />
        <button
          type="button"
          onClick={() => setShowPassword(prev => !prev)}
          style={{
            position: 'absolute',
            top: '50%',
            right: '0.9rem',
            transform: 'translateY(-50%)',
            background: 'none',
            border: 'none',
            cursor: 'pointer',
            color: 'var(--secondary)',
            opacity: 0.75,
            lineHeight: 1,
            padding: 0,
          }}
          tabIndex={-1}
          aria-label={showPassword ? 'Ocultar contraseña' : 'Mostrar contraseña'}
        >
          <span className="material-symbols-outlined" style={{ fontSize: '1.3rem', userSelect: 'none' }}>
            {showPassword ? 'visibility_off' : 'visibility'}
          </span>
        </button>
      </div>
    </Form.Group>
  );
}
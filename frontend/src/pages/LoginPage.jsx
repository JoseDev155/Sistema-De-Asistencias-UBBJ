import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Row, Col, Form, Button, Alert } from 'react-bootstrap';
import { fetchApi } from '@/api/apiFunctions';
import { useAuth } from '@/context/AuthContext';
import LoginHeroPanel from '@/components/LoginHeroPanel';
import PasswordField from '@/components/PasswordField';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const { setToken } = useAuth();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const data = await fetchApi('/auth/login', {
        method: 'POST',
        body: JSON.stringify({ username: email, password: password }),
      });

      localStorage.setItem('accessToken', data.access_token);
      setToken(data.access_token);  // actualiza el contexto sin recarga
      navigate('/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container fluid className="vh-100 d-flex align-items-center justify-content-center" style={{ backgroundColor: 'var(--background)' }}>
      <Row className="w-100 shadow-lg rounded overflow-hidden" style={{ maxWidth: '1000px', backgroundColor: 'var(--surface)' }}>
        <Col lg={6}>
          <LoginHeroPanel />
        </Col>

        <Col lg={6} xs={12} className="p-sm-5 p-4 d-flex align-items-center">
          <div className="w-100">
            <div className="mb-4 d-flex align-items-center d-lg-none">
              <span className="material-symbols-outlined fs-4 text-primary me-2">account_balance</span>
              <h5 className="headline fw-bold mb-0 text-primary">Sistema de Asistencias</h5>
            </div>
            <h2 className="headline fw-bold mb-1">Formulario de Acceso</h2>
            <p className="text-secondary mb-4">Autenticación Institucional Requerida</p>

            {error && <Alert variant="danger">{error}</Alert>}

            <Form onSubmit={handleLogin}>
              <Form.Group className="mb-4">
                <Form.Label className="text-secondary text-uppercase fw-bold" style={{ fontSize: '0.8rem', letterSpacing: '1px' }}>ID o Correo Electrónico</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="correo@ejemplo.edu.mx"
                  className="bg-dark text-light border-secondary p-3"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </Form.Group>

              <PasswordField
                id="input-login-password"
                label="Clave de Acceso"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />

              <div className="d-grid mt-5">
                <Button variant="danger" size="lg" type="submit" className="text-uppercase fw-bold border-0 p-3" disabled={loading}>
                  {loading ? 'Autenticando...' : 'Autenticar credenciales'}
                </Button>
              </div>
            </Form>
            <div className="mt-5 text-center">
              <small className="text-secondary opacity-75">
                Solo Personal Autorizado. Todos los intentos de acceso son registrados.
              </small>
            </div>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

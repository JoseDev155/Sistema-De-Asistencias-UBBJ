import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Row, Col, Form, Button, Alert } from 'react-bootstrap';
import { fetchApi } from '@/api/apiFunctions';
import { useAuth } from '@/context/AuthContext';
import LoginHeroPanel from '@/components/LoginHeroPanel';
import PasswordField from '@/components/PasswordField';
import mexicoLogo from '@/assets/mexico.svg';

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
    <Container
      fluid
      className="login-page d-flex align-items-center justify-content-center"
      style={{ backgroundColor: 'var(--login-bg)' }}
    >
      <Row className="login-shell w-100 g-0 overflow-hidden">
        <Col lg={5} className="d-none d-lg-block">
          <LoginHeroPanel />
        </Col>

        <Col lg={7} xs={12} className="login-form-panel d-flex align-items-center">
          <div className="login-form-inner w-100">
            <div className="d-flex align-items-center gap-3 mb-4 d-lg-none">
              <img src={mexicoLogo} alt="UBBJ" className="login-mobile-logo" />
              <div>
                <p className="login-mobile-kicker mb-0">Sistema institucional</p>
                <h5 className="text-danger headline fw-bold mb-0">UBBJ</h5>
              </div>
            </div>

            <div className="login-brand-chip mb-4">
              <span className="material-symbols-outlined">account_balance</span>
              <span>Sistema de Asistencias - UBBJ</span>
            </div>

            <h2 className="login-title headline fw-bold mb-2">Iniciar sesión</h2>
            <p className="login-subtitle mb-4">Acceso institucional para docentes y administradores.</p>

            {error && <Alert variant="danger">{error}</Alert>}

            <Form onSubmit={handleLogin}>
              <Form.Group className="mb-4">
                <Form.Label className="text-uppercase fw-bold login-label" style={{ fontSize: '0.8rem', letterSpacing: '1px' }}>ID o Correo Electrónico</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="correo@ejemplo.edu.mx"
                  className="login-input login-input-light p-3"
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
                variant="light"
              />

              <div className="d-grid mt-5">
                {/* Se elimino login-submit de className */}
                <Button variant="danger" size="lg" type="submit" className="text-uppercase fw-bold border-0 p-3" disabled={loading}>
                  {loading ? 'Autenticando...' : 'Autenticar credenciales'}
                </Button>
              </div>
            </Form>

            <div className="login-bottom-note mt-4">
              <span className="material-symbols-outlined">verified_user</span>
              <small>Solo personal autorizado. Todos los intentos de acceso son registrados.</small>
            </div>
          </div>
        </Col>
      </Row>
    </Container>
  );
}

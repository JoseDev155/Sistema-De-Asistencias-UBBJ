import mexicoLogo from '@/assets/mexico.svg';
import bannerImage from '@/assets/Banner_UBBJ.png';

export default function LoginHeroPanel() {
  return (
    <div
      className="login-hero d-none d-lg-flex"
      style={{ backgroundImage: `linear-gradient(145deg, rgba(18, 4, 10, 0.9), rgba(86, 14, 42, 0.72)), url(${bannerImage})` }}
    >
      <div className="login-hero-inner">
        <div className="login-hero-brand">
          <img src={mexicoLogo} alt="UBBJ" className="login-hero-logo" />
          <div>
            <p className="login-hero-kicker mb-1">Sistema institucional</p>
            <h1 className="login-hero-title mb-0">Universidad para el Bienestar Benito Juárez García</h1>
          </div>
        </div>

        <p className="login-hero-copy mb-0">
          Registro de asistencias, reportes y control académico con acceso exclusivo para personal autorizado.
        </p>

        <div className="login-hero-stats">
          <div>
            <span className="login-hero-stat-label">Módulos</span>
            <strong>Académicos</strong>
          </div>
          <div>
            <span className="login-hero-stat-label">Acceso</span>
            <strong>Institucional</strong>
          </div>
        </div>
      </div>

      <div className="login-hero-footer">
        <span className="material-symbols-outlined">lock</span>
        <span>Acceso seguro para profesores y administradores</span>
      </div>
    </div>
  );
}
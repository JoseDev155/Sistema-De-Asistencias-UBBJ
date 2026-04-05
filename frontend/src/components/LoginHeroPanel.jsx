export default function LoginHeroPanel() {
  return (
    <div className="d-none d-lg-flex flex-column justify-content-between p-5 text-light" style={{ borderRight: '1px solid #3e4042' }}>
      <div>
        <div className="d-flex align-items-center mb-4">
          <span className="material-symbols-outlined fs-2 text-primary me-2">account_balance</span>
          <h4 className="headline fw-bold mb-0 text-primary">Sistema de Asistencias</h4>
        </div>
        <h1 className="headline display-5 fw-bold mt-5">
          Universidades para el Bienestar Benito Juárez García <br />
          <span className="text-primary">(UBBJ)</span>
        </h1>
        <p className="mt-4 text-secondary fs-5" style={{ fontWeight: 300 }}>
          Integridad académica, archivada digitalmente. Seguro, inmutable y permanente.
        </p>
      </div>
      <div className="d-flex gap-5 mt-5 pt-5">
        <div>
          <p className="text-primary fw-bold text-uppercase mb-1" style={{ fontSize: '0.8rem', letterSpacing: '2px' }}>Establecido</p>
          <h5 className="headline text-light">1894</h5>
        </div>
        <div>
          <p className="text-primary fw-bold text-uppercase mb-1" style={{ fontSize: '0.8rem', letterSpacing: '2px' }}>Versión</p>
          <h5 className="headline text-light">v1.0.4 - ESTABLE</h5>
        </div>
      </div>
    </div>
  );
}
import { Modal, Button, Form, Spinner, Alert } from 'react-bootstrap';

export default function CrudModal({
  show,
  onHide,
  title,
  onSubmit,
  error,
  children,
  submitLabel,
  savingLabel = 'Procesando...',
  saving = false,
  submitId,
}) {
  return (
    <Modal show={show} onHide={onHide} centered data-bs-theme="dark">
      <Modal.Header closeButton style={{ background: 'var(--surface)', borderColor: 'var(--border)' }}>
        <Modal.Title className="headline" style={{ fontSize: '1.1rem' }}>
          {title}
        </Modal.Title>
      </Modal.Header>
      <Form onSubmit={onSubmit}>
        <Modal.Body style={{ background: 'var(--surface)' }}>
          {error && <Alert variant="danger" className="py-2">{error}</Alert>}
          {children}
        </Modal.Body>
        <Modal.Footer style={{ background: 'var(--surface)', borderColor: 'var(--border)' }}>
          <Button variant="outline-secondary" onClick={onHide}>
            Cancelar
          </Button>
          <Button id={submitId} type="submit" variant="danger" disabled={saving}>
            {saving ? <><Spinner size="sm" animation="border" className="me-2" />{savingLabel}</> : submitLabel}
          </Button>
        </Modal.Footer>
      </Form>
    </Modal>
  );
}
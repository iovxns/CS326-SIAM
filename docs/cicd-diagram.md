# CI/CD Diagram

```mermaid
graph TD
    A[Push to Main] --> B[GitHub Action Triggered]
    B --> C[Deploy Step]
    C --> D[Smoke Test]
    D -- Success --> E[Live App Verified]
    D -- Failure --> F[Notify Developer]
"""Entry point – starts the PCI-DLI API server."""
import os
import uvicorn

if __name__ == "__main__":
    host = os.environ.get("PCI_HOST", "0.0.0.0")
    port = int(os.environ.get("PCI_PORT", "8000"))
    uvicorn.run("pci_dli_api:app", host=host, port=port, reload=False)

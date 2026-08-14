"""Entry point – starts the PCI-DLI API server."""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("pci_dli_api:app", host="0.0.0.0", port=8000, reload=False)

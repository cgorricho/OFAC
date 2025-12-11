"""Entry point for running OFAC screening tools.

Usage:
    python -m ofac              # Start API server
    python -m ofac --help       # Show help
"""

import argparse
import sys

from ofac import __version__


def main() -> int:
    """Main entry point for the OFAC screening tools."""
    parser = argparse.ArgumentParser(
        description="OFAC Sanctions Screening Tools for Humanitarian NGOs",
        prog="ofac",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--api",
        action="store_true",
        help="Start the FastAPI server (default)",
    )
    parser.add_argument(
        "--streamlit",
        action="store_true",
        help="Start the Streamlit application",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to (default: 8000 for API, 8501 for Streamlit)",
    )

    args = parser.parse_args()

    if args.streamlit:
        # Streamlit mode - to be implemented
        print("Streamlit application not yet implemented. Coming in Epic 2.")
        return 1

    # Default: Start API server
    print(f"Starting OFAC API server on {args.host}:{args.port}")
    print("API server not yet implemented. Coming in Epic 2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())


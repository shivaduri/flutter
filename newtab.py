import sys

def main(argv):
    try:
        # Simulate some logic that might raise an exception
        raise Exception("Simulated error for demonstration")
    except Exception as e:
        # ✅ Corrected: use str(e) instead of e.message
        sys.stderr.write(str(e) + '\n\n')
        return 1

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    sys.exit(main(sys.argv))

from website import create_app

isHome = True

def main():
    # Create application
    app = create_app()
    if app == None: return

    app.run(debug=True, host='0.0.0.0', port=8080)
    print("no lmao")

    print("Flask app shutting down.")

if __name__ == "__main__":
    main()
def bonjour():
    print("Bonjour du module B")
    print(__name__)
# Ceci sera exécuté lors de l'import de ce module
print("Salut")

# Ceci ne sera pas exécuté lors de l'import du module
if __name__ == "__main__":
    print("Module module_.py")
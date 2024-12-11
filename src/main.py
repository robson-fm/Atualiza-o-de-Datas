from views.main_view import MainView
from controllers.app_controller import AppController

if __name__ == "__main__":
    # Inicialize o controlador, passando a view para ele (se necessário)
    # Inicializa o controlador sem a view inicialmente
    controller = AppController(None)

    # Agora, passe o controlador para a view
    # A view agora recebe o controlador corretamente
    view = MainView(controller)
    # Atualize o controlador para apontar para a view corretamente
    # Isso garante que o controlador tenha a referência para a view
    controller.view = view
    # Execute o aplicativo
    view.run()

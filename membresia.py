# Importar metodo abstracto 
from abc import ABC, abstractmethod

class Membresia(ABC):
    """ 
    Clase abstracta base para las diferentes membresías.
    """
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """ Inicializa una nueva instancia de la clase.
        
        Args:
            correo_suscriptor (str): Cadena de texto correspondiente al correo electrónico del suscriptor de la membresía.
            numero_tarjeta (str): Cadena de texto correspondiente al número de la tarjeta de crédito/débito asociada a la membresía.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        """ Metodo que retorna el correo del suscriptor.

        Returns:
            str: Retorna la cadena de texto correspondiente al correo del suscriptor
        """
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        """ Metodo que retorna el número de tarjeta del suscriptor.

        Returns:
            str: Retorna la cadena de texto correspondiente al número de tarjeta del suscriptor
        """
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo abstracto para cambiar el tipo de membresía.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.
        """
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        """ Metodo que crea y retorna una nueva instancia de membresía basada en el tipo especificado.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.

        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador de la membresia para su creación.
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    """ Clase que representa una membresía Gratis.

    Args:
        Membresia (class): Clase de la que se heredan sus metodos y atributos.
    """
    costo_suscripcion = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo que cambia el tipo de membresía a un nivel distinto.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.

        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador para el cambio de membresia.
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class Basica(Membresia):
    """ Clase que representa una membresía Básica.

    Args:
        Membresia (class): Clase de la que se heredan sus metodos y atributos.
    """
    costo_suscripcion = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """ Metodo que inicializa una membresía básica con el correo electrónico y número de tarjeta proporcionados.

        Args:
            correo_suscriptor (str): Cadena de texto correspondiente al correo electrónico del suscriptor de la membresía.
            numero_tarjeta (str): Cadena de texto correspondiente al número de la tarjeta de crédito/débito asociada a la membresía.
        """
        super().__init__(correo_suscriptor, numero_tarjeta)
        # Asignacion de días de regalo según corresponda
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        elif isinstance(self, Pro):
            self.__dias_regalo = 15

    def cancelar_suscripcion(self):
        """ Metodo que cancela la suscripción actual.

        Returns:
            object: Retorna una nueva instancia de membresía gratuita.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo que cambia el tipo de membresía a un nivel distinto.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.
            
        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador para el cambio de membresia.
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


class Familiar(Basica):
    """ Clase que representa una membresía Familiar.

    Args:
        Basica (class): Clase de la que se heredan sus metodos y atributos.
    """
    costo_suscripcion = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo que cambia el tipo de membresía a un nivel distinto.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.

        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador para el cambio de membresia.
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def modificar_control_parental(self):
        """ 
        Metodo reservado para modificar la configuración de control parental.
        """
        pass


class SinConexion(Basica):
    """ Clase que representa una membresía Sin Conexión.

    Args:
        Basica (class): Clase de la que se heredan sus metodos y atributos.
    """
    costo_suscripcion = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo que cambia el tipo de membresía a un nivel distinto.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.

        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador para el cambio de membresía.
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        """ 
        Metodo reservado para modificar la cantidad maxima permitada en offline.
        """
        pass


class Pro(Familiar, SinConexion):
    """ Clase que representa una membresía Pro.

    Args:
        SinConexion (class): Clase de la que se heredan sus metodos y atributos.
    """
    costo_suscripcion = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """ Metodo que cambia el tipo de membresía a un nivel distinto.

        Args:
            nueva_membresia (int): Corresponde al identificador numérico del nuevo tipo de membresía.

        Returns:
            object: Retorna una nueva instancia de la membresía correspondiente al identificador.
        """
        # Validador del identificador para el cambio de membresía.
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)


g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))

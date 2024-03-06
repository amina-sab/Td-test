import pytest
from unittest.mock import MagicMock
from CartePizzeria import CartePizzeria, CartePizzeriaException

def test_is_empty():
    carte_pizza=CartePizzeria()
    assert carte_pizza.is_empty()==True

    pizza_mock=MagicMock()
    pizza_mock.add(Campionne)
    assert pizza_mock.is_empty()==False

def test_nb_pizzas():
    carte_pizza=CartePizzeria()
    assert carte_pizza.nb_pizzas==0 

    pizza_mock=MagicMock()
    pizza_mock.add(Campionne)
    pizza_mock.add(Marguarita)
    assert pizza_mock.nb_pizzas==2 

def test_add_pizza():
    carte_pizza=CartePizzeria()
    pizza_mock=MagicMock()
    pizza_mock.add_pizza(Campionne)
    assert pizza_mock.nb_pizza()==1

def test_remove_pizza():
    carte_pizza=CartePizzeria
    pizza_mock_1=MagicMock()
    pizza_mock_1.name="vegetarienne"
    pizza_mock_2=MagicMock()
    pizza_mock_2.name="marguarita"
    carte_pizza.add(pizza_mock_1)  
    carte_pizza.add(pizza_mock_2) 
    
    carte_pizza.remove_pizza(pizza_mock_1)
    assert carte_pizza.nb_pizzas==1

    with pytest.raises(CartePizzeriaException):
        carte_pizza.remove_pizza("Hawaiiane")

import pytest
from brownie import SimpleCounter, accounts
from brownie.network import priority_fee

@pytest.fixture
def simple_counter():
    priority_fee('0.1 gwei') #important
    return SimpleCounter.deploy({'from': accounts[0]})

def test_increment(simple_counter):
    # Get the initial counter value
    initial_counter_value = simple_counter.getCounter()

    # Call the increment function
    simple_counter.increment()

    # Get the new counter value
    new_counter_value = simple_counter.getCounter()

    # Assert that the counter was incremented by 1
    assert new_counter_value == initial_counter_value + 1

def test_decrement(simple_counter):
    # Get the initial counter value
    initial_counter_value = simple_counter.getCounter()

    # Call the decrement function
    simple_counter.increment()
    simple_counter.increment()
    simple_counter.increment()
    simple_counter.decrement()

    # Get the new counter value
    new_counter_value = simple_counter.getCounter()

    # Assert that the counter was decremented by 1
    assert new_counter_value == initial_counter_value + 2

def test_cannot_decrement_below_zero(simple_counter):

    # Call the decrement function until the counter is at 0
    while simple_counter.getCounter() > 0:
        simple_counter.decrement()

    # Try to decrement below zero
    with pytest.raises(Exception):
        simple_counter.decrement()
    
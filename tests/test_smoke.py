from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")

def test_training_keyword_only():
    assert "I.101" in reply("training")

def test_training_in_sentence():
    assert "I.101" in reply("Where is training?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."

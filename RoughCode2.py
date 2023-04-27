import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample:
    def editProfile(self,dataLoad):
        print(dataLoad[0])
        print("Enter")

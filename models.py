from pydantic import Field, BaseModel


class ColorPallet(BaseModel):
    text: str = Field(description="Color of text should contrast from background color on the page which follows the theme in hexadecimal format.")
    background: str = Field(description="Background color of the page which follows the theme in hexadecimal format.")
    primary: str = Field(description="Primary color of the page which follows the theme in hexadecimal format.")
    secondary: str = Field(description="Secondary color of the page which follows the theme in hexadecimal format.")
    accent: str = Field(description="Accent of the theme of the page which follows the theme in hexadecimal format.")
    reason: str = Field(description="Reason for the color pallet and how it follows the theme")

    def __str__(self):
        return f"Text: {self.text}\nBackground: {self.background}\nPrimary: {self.primary}\nSecondary: {self.secondary}\nAccent: {self.accent}"


class FreeformColorPallet(BaseModel):
    colors: list[str] = Field(description="colors generated which follow a theme")

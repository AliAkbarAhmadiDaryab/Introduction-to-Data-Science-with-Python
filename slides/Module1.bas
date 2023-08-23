Attribute VB_Name = "Module1"
Sub CreatePythonPresentation()
    Dim pptApp As Object
    Dim pptPresentation As Object
    Dim pptSlide As Object
    
    ' Create a new PowerPoint application
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    ' Add a new presentation
    Set pptPresentation = pptApp.Presentations.Add
    
    ' Slide 1: Introduction
    Set pptSlide = pptPresentation.Slides.Add(1, ppLayoutTitle)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Introduction to Python Programming for Beginners"
    
    ' Slide 2: Setting Up Python
    Set pptSlide = pptPresentation.Slides.Add(2, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Setting Up Python"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Installing Python on Windows, macOS, Linux" & vbCrLf & "Introduction to IDLE"
    
    ' Slide 3: Your First Python Program
    Set pptSlide = pptPresentation.Slides.Add(3, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Your First Python Program"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Show code: print(""Hello, World!"")" & vbCrLf & "Run the program in IDLE"
    
    ' Slide 4: Variables and Data Types
    Set pptSlide = pptPresentation.Slides.Add(4, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Variables and Data Types"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Variables and their purpose" & vbCrLf & _
                                                            "Common data types: int, float, string, boolean" & vbCrLf & _
                                                            "Example of variable assignments"
    
     ' Slide 5:  Basic Operations
    Set pptSlide = pptPresentation.Slides.Add(5, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Basic Operations"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Explain arithmetic operations (+, -, *, /)"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Show examples of calculations using variables"
    
      ' Slide 6: Conditional Statements
    Set pptSlide = pptPresentation.Slides.Add(6, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Conditional Statements"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Introduce if statements for decision-making" & vbCrLf & "Show examples of using if, elif, and else"
    
    ' Slide 7: Loops
    Set pptSlide = pptPresentation.Slides.Add(7, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Loops"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Introduce loops (for and while)" & vbCrLf & "Explain how loops are used for repetitive tasks" & vbCrLf & "Show examples of using for and while loops"
    
    ' Slide 8: Lists and Arrays
    Set pptSlide = pptPresentation.Slides.Add(8, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Lists and Arrays"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Explain lists as collections of items" & vbCrLf & "Creating, accessing, and modifying list elements"
    
    ' Slide 9: Functions
    Set pptSlide = pptPresentation.Slides.Add(9, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Functions"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Introduction to functions and their purpose" & vbCrLf & "Examples of creating and using functions"
    
    ' Slide 10: Variables and Data Types
    Set pptSlide = pptPresentation.Slides.Add(10, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Libraries and Modules"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Introduction to libraries and modules" & vbCrLf & "Mention common libraries like math and random" & vbCrLf & "Importing and using functions from libraries"

    
    ' Slide 11: Input and Output
    Set pptSlide = pptPresentation.Slides.Add(11, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Input and Output"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Taking user input" & vbCrLf & "Displaying output to the user"
    
    ' Slide 12: Conclusion
    Set pptSlide = pptPresentation.Slides.Add(12, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Conclusion"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Recap of key concepts" & vbCrLf & "Encouragement for further learning" & vbCrLf & "Resources for learning more about Python"

    
    ' Slide 13: Q&A
    Set pptSlide = pptPresentation.Slides.Add(13, ppLayoutText)
    pptSlide.Shapes.Title.TextFrame.TextRange.Text = "Q&A"
    pptSlide.Shapes.Placeholders(2).TextFrame.TextRange.Text = "Encourage participants to ask questions. Be ready for some Python humor!"
    
    ' Clean up
    Set pptSlide = Nothing
    Set pptPresentation = Nothing
    Set pptApp = Nothing
End Sub


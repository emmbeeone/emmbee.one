$word = New-Object -ComObject Word.Application
$word.Visible = $false

$doc1Path = (Resolve-Path ".\CASE-STUDY_Student.docx").Path
$doc1 = $word.Documents.Open($doc1Path)
$doc1.Content.Text | Out-File -FilePath ".\CASE-STUDY_Student.txt" -Encoding UTF8
$doc1.Close()

$doc2Path = (Resolve-Path ".\Meet the Mentors.docx").Path
$doc2 = $word.Documents.Open($doc2Path)
$doc2.Content.Text | Out-File -FilePath ".\Meet_the_Mentors.txt" -Encoding UTF8
$doc2.Close()

$word.Quit()
Write-Host "Done"

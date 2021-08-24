Write-Host "Please enter the first number."
$FIRST_NUM = Read-Host
Write-Host "Please enter the second number."
$SECOND_NUM = Read-Host
$SUM = $FIRST_NUM + $SECOND_NUM
$SUB = $FIRST_NUM - $SECOND_NUM
$MUL = [int]$FIRST_NUM * [int]$SECOND_NUM
$DIV = $FIRST_NUM / $SECOND_NUM
Write-Host $FIRST_NUM "+" $SECOND_NUM "=" $SUM
Write-Host $FIRST_NUM "-" $SECOND_NUM "=" $SUB
Write-Host $FIRST_NUM "*" $SECOND_NUM "=" $MUL
Write-Host $FIRST_NUM "/" $SECOND_NUM "=" $DIV
New-Item -Path "results.txt" -ItemType File
Set-Content .\results.txt $SUM
Add-Content .\results.txt $SUB
Add-Content .\results.txt $MUL
Add-Content .\results.txt $DIV
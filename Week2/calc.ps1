New-Item -Path "results.txt" -ItemType File
Write-Host "Please enter the first number."
$FIRST_NUM = Read-Host
Write-Host "Please enter the second number."
$SECOND_NUM = Read-Host
$SUM = [int]$FIRST_NUM + [int]$SECOND_NUM
$SUB = [int]$FIRST_NUM - [int]$SECOND_NUM
$MUL = [int]$FIRST_NUM * [int]$SECOND_NUM
if ( ( 0 -ne $FIRST_NUM ) -and ( 0 -ne $SECOND_NUM ) )
{
$DIV = [int]$FIRST_NUM / [int]$SECOND_NUM
}
Write-Host $FIRST_NUM "+" $SECOND_NUM "=" $SUM
Write-Host $FIRST_NUM "-" $SECOND_NUM "=" $SUB
Write-Host $FIRST_NUM "*" $SECOND_NUM "=" $MUL
Set-Content .\results.txt $SUM
Add-Content .\results.txt $SUB
Add-Content .\results.txt $MUL
if ( 0 -eq $FIRST_NUM )
{
Write-Host "It is not possible to divide with 0"
}
elseif ( 0 -eq $SECOND_NUM )
{
Write-Host "It is not possible to divide with 0"
}
else
{
Write-Host $FIRST_NUM "/" $SECOND_NUM "=" $DIV
Add-Content .\results.txt $DIV
}

#Command to run every 30 seconds is watch --interval 30 [File Path]

if [ ! -d "/processes" ];
then
mkdir processes
fi
datetime=$(date)
touch processes/"$datetime"
ps -ef > processes/"$datetime"


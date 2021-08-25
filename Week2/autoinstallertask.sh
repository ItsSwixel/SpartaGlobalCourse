echo "Please enter a username."
read USERNAME
echo "Please enter a password."
read -s PASSWORD
echo "Please enter a directory name."
read DIRECTORY
pwd
mkdir $DIRECTORY
touch $DIRECTORY/cyber.log
pwd > $DIRECTORY/cyber.log
whoami >> $DIRECTORY/cyber.log
date >> $DIRECTORY/cyber.log
echo $USERNAME >> $DIRECTORY/cyber.log
echo $PASSWORD >> $DIRECTORY/cyber.log
echo "Please enter the number of packages to install."
read PACKAGE_NUMBER
echo $PACKAGE_NUMBER >> $DIRECTORY/cyber.log
for ((i=1; i<=$PACKAGE_NUMBER; i++));
do
echo "Please enter the name of the package."
read PACKAGE_NAME
touch $DIRECTORY/$PACKAGE_NAME.log
echo $PACKAGE_NAME >> $DIRECTORY/cyber.log
sudo apt-get install $PACKAGE_NAME -y > $DIRECTORY/$PACKAGE_NAME.log
done

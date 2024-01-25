#!/bin/bash

'''
1-) Bash script part:
    1.a-)If there is a file under the /var/lib/mysql-files/ directory read the file
            1.a.1-) If the file has the string 'dropped' under the index[6]:
                    break
                else:
                  1.a.1.a-)  If the file has been created and 'dropped' string has not written into the file yet
                    trigger the rundeck job
         else:
            trigger the mysql.sql and create the file. Has to trigger rundex job or return value that rundeck 
            job can move on
'''
!/bin/bash

sysdate=$(date +%d%m%Y)

mysql_user="root"
mysql_password="vatiku41"

mysql_script="/root/scripts/mysql.sql"
output_path="/var/lib/mysql-files/"
output_file="${output_path}vm_state_${sysdate}.out"

if [ -e "$output_file" ]; then
    if grep -q "drop" "$output_file"; then
        echo "false"
    else
        echo "true"
    fi
else
    mysql -u$mysql_user  -p$mysql_password < $mysql_script | sed 's/\t/,/g' >> "$output_file"
fi


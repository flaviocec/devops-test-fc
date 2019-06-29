pckage 'httpd' do
    case node[:platform]
    when 'redhat', 'centos'
      package_name 'httpd'
    when 'ubuntu', 'debian'
      package_name 'apache2'
    end
    action :install
end

service 'httpd' do
    action [:enable, :start]
end

file '/etc/motd' do
    owner 'root'
    group 'root'
    mode '0644'
    content 'Hello world'
end

user 'flavio.ceccarelli' do
    home '/home/flavioc'
    shell '/bin/bash'
    password 'MyPassword19'
end

timezone 'Europe/London' do
    action :set
end

cron 'flavio-cron-job' do
    action :create
    minute '45'
    hour '5'
    day '*'
    user 'root'
    home '/home/ec2-user'
    command '/bin/true'
end

package 'httpd' do
    action install
end

file '/etc/motd'
    owner 'root'
    group 'root'
    mode '0644'
    content 'Hello world'
end

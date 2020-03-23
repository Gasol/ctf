#!/usr/bin/ruby
require 'cgi'

cgi = CGI::new
program = cgi['program']

result = ""
message = ""
unless program != ""
  message = ""
else
  program=program.to_s.gsub("\r","")
  if /\A[a-z \r\n]+\Z/ =~ program && program.split("\n").size <= 25
    begin
      result = eval(program)
    rescue Exception => e
      message = "Program Error"
    end
  else
    message = "Cannot run the program."
  end
end

cgi.out do
  <<EOL
<!doctype html>
<html lang="en">
  <head>
    <title>Alphabet Programming</title>
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
      <h3>Program</h3>
      <div class="span12">
        <form method="post" class="form">
          <div class="form-group">
          <label>Program</label>
          <textarea class="form-control" name="program">#{CGI.escapeHTML(program)}</textarea>
          </div>
          <input type="submit" class="btn btn-primary">
        </form>
      </div>
      <h3>Result</h3>
      <div style="color:red;">#{message}</div>
      <pre>#{CGI.escapeHTML(result.to_s)}</pre>
    </div>
  </body>
</html>
EOL
end

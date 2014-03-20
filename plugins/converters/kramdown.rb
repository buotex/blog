class Ruhoh
  module Converter
    module Markdown
      def self.extensions
        ['.md', '.markdown']
      end
      def self.convert(content)
        require 'kramdown'
        Kramdown::Document.new(content, :input => 'GFM').to_html
      end
    end
    module Todo
      def self.extensions
        ['.todo']
      end
      def self.convert(content)

        #filename = @page_data['url']
        #prefix = "<a href=\"/api?post=#{filename}&number="
        # command = 'javascript:setTimeout(\'history.go(0)\',2000); javascript:event.target.port=8888;'
        #command = 'javascript:event.target.port=8888;'
        #postfix= "\" onclick=\"#{command}\">\u2610</a>"
        #block = sub_context.gsub(/\[[^+]?\]/).with_index { |m, i| "#{prefix}#{1+i}#{postfix}" }
        content = content.gsub(/^/, "<li>\u2610")
        content = content.gsub(/$/, '</li>')
        content = "<ul>" + content
        content = content + "</ul>"
      end
    end
    module Todolist
      def self.extensions
        ['.todolist']
      end
      def self.convert(content)
      
        prefix = "<a href=\"/todo?project=&context=&cache=\ \" class=\"lightview\" 
        data-lightview-type=\"iframe\" "
        command = 'javascript:event.target.port=8889;'
        postfix= "onclick=\"#{command}\">Show All</a>"
        res = prefix + postfix
        
        #filename = @page_data['url']
        #prefix = "<a href=\"/api?post=#{filename}&number="
        #postfix= "\" onclick=\"#{command}\">\u2610</a>"
        #block = sub_context.gsub(/\[[^+]?\]/).with_index { |m, i| "#{prefix}#{1+i}#{postfix}" }
        #content = content.gsub(/^/, "<li>\u2610")
        #content = content.gsub(/$/, '</li>')
        #content = "<ul>" + content
        #content = content + "</ul>"
      end
    end
  end
end

module PagesModelViewAddons


	def todo_block(sub_context)
		filename = @page_data['url']
		prefix = "<a href=\"/api?post=#{filename}&number="
    # command = 'javascript:setTimeout(\'history.go(0)\',2000); javascript:event.target.port=8888;'
    command = 'javascript:event.target.port=8888;'
		postfix= "\" onclick=\"#{command}\">\u2610</a>"
		block = sub_context.gsub(/\[[^+]?\]/).with_index { |m, i| "#{prefix}#{1+i}#{postfix}" }
	end
end

#Ruhoh.collections('pages').send(:include, PagesModelViewAddons)
Ruhoh::Views::MasterView.__send__(:include, PagesModelViewAddons)



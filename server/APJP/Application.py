# APJP, A PHP/JAVA PROXY
# Copyright (C) 2009-2012 Jeroen Van Steirteghem
# 
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import HTTP
import HTTPS
import webob
import errno


class Application():
  def __call__(self, environ, start_response):    
    request = webob.Request(environ)
    
    if 0 > request.path_info.find('HTTPS') :
      application = HTTP.Application()
      return application(environ, start_response)
    else:
      application = HTTPS.Application()
      return application(environ, start_response)
  
    response = webob.Response(None, 200, None, None)
    return response(environ, start_response)
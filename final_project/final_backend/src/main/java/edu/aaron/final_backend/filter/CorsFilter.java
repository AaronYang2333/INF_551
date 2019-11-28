package edu.aaron.final_backend.filter;

import org.springframework.stereotype.Component;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * @author Aaron Yang (yb)
 * @version 1.0
 * @modified Aaron 2017/11/22 16:36
 * @email aaron19940628@gmail.com
 * @date 2017/11/22 16:36.
 * @description 服务端允许跨域
 */
@Component
public class CorsFilter implements Filter {

    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
        HttpServletResponse response = (HttpServletResponse) res;
        HttpServletRequest request = (HttpServletRequest) req;
        String curOrigin = request.getHeader("Origin");

        if (curOrigin != null) {
            //允许访问该资源的外域 URI
            response.setHeader("Access-Control-Allow-Origin", curOrigin);
            //服务器允许客户端使用POST, GET, OPTIONS, DELETE, PUT, HEAD等方法
            response.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE,PUT,HEAD");
            //响应时间
            response.setHeader("Access-Control-Max-Age", "3600");
            //预检请求的响应,设置为true
            response.setHeader("Access-Control-Allow-Credentials", "true");
            //服务器允许请求中携带字段
            response.setHeader("Access-Control-Allow-Headers", "x-requested-with,X-AUTH-USER, X-AUTH-TOKEN,Origin,Content-Type, Accept");
        }
        chain.doFilter(req, res);
    }

    public void init(FilterConfig filterConfig) {
    }

    public void destroy() {
    }
}

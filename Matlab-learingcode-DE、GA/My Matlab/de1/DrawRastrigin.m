function DrawRastrigin()
    % 绘制2维Rastrigin函数图形
    x = [-5 : 0.05 : 5 ];
    y = x;
    [X,Y] = meshgrid(x,y);
    [row,col] = size(X);
    for  l = 1 :col
         for  h = 1 :row
            z(h,l) = ras([X(h,l),Y(h,l)]);
        end
    end
    
    figure
    mesh(X,Y,z)
    hold on
    contour(X,Y,z)
    shading interp
end

% function y = Rastrigin(x)
%     [row,~] = size(x);
%     if  row > 1 
%         error( ' 输入的参数错误 ' );
%     end
%     y = sum(x.^2 - 10 * cos( 2 * pi * x) + 10 );
%     y =y;
% end
function s = ras(pop)
%RASTRIGINSFCN Compute the "Rastrigin" function.

%   Copyright 2003-2004 The MathWorks, Inc.


    % pop = max(-5.12,min(5.12,pop));
    s=10*size(pop,2)+sum(pop.^2 -10*cos(2*pi.*pop),2);
end
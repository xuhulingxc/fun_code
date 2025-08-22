import math

def f(x):
    """定义函数 f(x) = e^x * ln(x) - x^2"""
    return math.exp(x) * math.log(x) - x**2

def bisection_method(a, b, tolerance=1e-5, max_iterations=100):
    """
    二分法求解方程的根
    
    参数:
    a, b: 区间端点
    tolerance: 容差
    max_iterations: 最大迭代次数
    
    返回:
    根的近似值
    """
    # 检查区间端点是否有根
    if f(a) * f(b) >= 0:
        raise ValueError("函数在区间端点同号，二分法无法使用")
    
    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        # 计算中点
        c = (a + b) / 2
        
        # 检查中点是否为根
        if abs(f(c)) < tolerance:
            return c
        
        # 确定新的区间
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iteration += 1
    
    # 返回最终近似值
    return (a + b) / 2

# 主程序
if __name__ == "__main__":
    try:
        # 设置区间和容差
        a, b = 1.0, 4.0
        tolerance = 1e-5
        
        # 使用二分法求解
        root = bisection_method(a, b, tolerance)
        
        print(f"方程 f(x) = e^x * ln(x) - x^2 = 0 在区间 [1, 4] 上的根为: {root:.6f}")
        print(f"函数值 f({root:.6f}) = {f(root):.6e}")
        print(f"误差: {abs(f(root)):.6e}")
        
    except ValueError as e:
        print(e)

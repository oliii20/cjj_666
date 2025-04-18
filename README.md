# 粒子群优化算法 (PSO) 实现

## 算法原理

粒子群优化算法 (Particle Swarm Optimization, PSO) 是一种基于群体智能的优化算法，灵感来自鸟群或鱼群的社会行为。算法通过模拟群体中个体的协作来寻找最优解。

### 主要概念

1. **粒子 (Particle)**: 每个粒子代表解空间中的一个潜在解
2. **位置 (Position)**: 粒子在解空间中的当前位置
3. **速度 (Velocity)**: 粒子移动的方向和速度
4. **个体最优 (Personal Best)**: 粒子自身找到的最优解
5. **全局最优 (Global Best)**: 整个群体找到的最优解

### 更新规则

1. **速度更新**: 
   ```
   v_i(t+1) = w * v_i(t) + c1 * r1 * (pbest_i - x_i(t)) + c2 * r2 * (gbest - x_i(t))
   ```
2. **位置更新**:
   ```
   x_i(t+1) = x_i(t) + v_i(t+1)
   ```

其中：
- w: 惯性权重
- c1, c2: 学习因子
- r1, r2: 随机数

## 实现特点

- 支持多维优化问题
- 可自定义粒子数量、迭代次数
- 包含边界处理机制
- 提供示例目标函数（Sphere函数）

## 使用说明

1. 定义目标函数
2. 设置搜索空间边界
3. 创建PSO实例
4. 调用optimize()方法进行优化

## 示例

```python
# 定义目标函数
def sphere(x):
    return sum([xi**2 for xi in x])

# 设置边界
bounds = [(-5, 5), (-5, 5)]

# 创建PSO实例
pso = PSO(sphere, bounds)

# 执行优化
best_position, best_fitness = pso.optimize()
```
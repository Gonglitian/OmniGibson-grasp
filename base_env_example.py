from envs.base_env import BaseEnv
from omnigibson.utils.ui_utils import KeyboardRobotController
from omnigibson.robots.robot_base import BaseRobot
from omnigibson.macros import gm
# 从debug模块导入调试功能
from utils.debug import setup_debug_keys
from pprint import pprint

# Do not use GPU dynamics, use flatcache to improve performance
gm.USE_GPU_DYNAMICS = False
gm.ENABLE_FLATCACHE = True
gm.ENABLE_TRANSITION_RULES = False
gm.ENABLE_OBJECT_STATES = False

def main():
    # 使用自定义环境类创建环境
    env = BaseEnv("config/scene_config.yaml")

    # 获取机器人实例
    robot: BaseRobot = env.robots[0]
    # print(f"robot.proprioception_dim: {robot.proprioception_dim}")
    # print(f"robot._proprio_obs: {robot._proprio_obs}")
    # pprint(robot._get_proprioception_dict())
    
    # 创建键盘控制器（确保键盘事件处理被注册）
    keyboard_controller = KeyboardRobotController(robot=robot)

    # 设置调试按键
    setup_debug_keys(keyboard_controller, robot, env)

    # 显示键盘控制信息
    keyboard_controller.print_keyboard_teleop_info()
    # robot name

    # 进入手动控制循环
    while True:
        # 获取键盘控制动作
        action = keyboard_controller.get_teleop_action()
        # 执行动作
        obs, reward, terminated, truncated, info = env.step(action)

        # print key of obs and its shape of value
        # pprint(obs[robot.name])
        # print(obs[robot.name].keys())


if __name__ == "__main__":
    main()

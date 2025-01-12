from typing import List

import constant as const
import tensorflow as tf
import tf_agents


def predict_observations_by_users(observation: List[List[float]]) -> List[int]:
    # Trained policy is saved in the ROOT_DIR, given observation
    # outputs action.
    # https://www.tensorflow.org/agents/tutorials/
    # 10_checkpointer_policysaver_tutorial#restore_checkpoint
    trained_policy = tf.saved_model.load(const.ROOT_DIR)

    # reference: https://github.com/yutsai84/vertex-ai-samples/
    # blob/ee6dd357320a9fb875750331c2558b510c8b316f/community-content/
    # tf_agents_bandits_movie_recommendation_with_kfp_and_vertex_sdk/
    # step_by_step_sdk_tf_agents_bandits_movie_recommendation/src/
    # prediction/main.py#L60-L63

    time_step = tf_agents.trajectories.restart(
        observation=observation,
        batch_size=tf.convert_to_tensor([const.BATCH_SIZE]),
    )
    action_step = trained_policy.action(time_step)
    return action_step.action.numpy().tolist()

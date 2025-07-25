# reviewer/rules.py

def get_comprehensive_rules():
    """Returns a dictionary containing all the rules for ML code analysis."""
    return {
        'data_leakage': {
            'patterns': [
                (r'(\w*test\w*).*\.fit_transform\(', 'fit_transform() on test data causes data leakage'),
                (r'scaler\.fit_transform\(.*test', 'Using fit_transform on test data - use transform() instead'),
                (r'imputer\.fit_transform\(.*test', 'Fitting imputer on test data causes leakage'),
                (r'encoder\.fit_transform\(.*test', 'Fitting encoder on test data causes leakage'),
                (r'selector\.fit_transform\(.*test', 'Fitting feature selector on test data causes leakage'),
                (r'pca\.fit_transform\(.*test', 'Fitting PCA on test data causes leakage'),
                (r'normalizer\.fit_transform\(.*test', 'Fitting normalizer on test data causes leakage'),
            ],
            'severity': 'critical'
        },
        'feature_scaling': {
            'scale_sensitive_algorithms': {
                'SVC': 'Support Vector Classifier', 'SVR': 'Support Vector Regression',
                'KNeighborsClassifier': 'K-Nearest Neighbors Classifier', 'KNeighborsRegressor': 'K-Nearest Neighbors Regression',
                'LogisticRegression': 'Logistic Regression', 'LinearRegression': 'Linear Regression',
                'Ridge': 'Ridge Regression', 'RidgeCV': 'Ridge Cross-Validation',
                'Lasso': 'Lasso Regression', 'LassoCV': 'Lasso Cross-Validation',
                'ElasticNet': 'Elastic Net Regression', 'SGDClassifier': 'Stochastic Gradient Descent Classifier',
                'SGDRegressor': 'Stochastic Gradient Descent Regressor', 'Perceptron': 'Perceptron',
                'MLPClassifier': 'Multi-layer Perceptron Classifier', 'MLPRegressor': 'Multi-layer Perceptron Regression',
            },
            'scalers': ['StandardScaler', 'MinMaxScaler', 'RobustScaler', 'MaxAbsScaler', 'PowerTransformer', 'QuantileTransformer', 'Pipeline'],
            'severity': 'warning'
        },
        'validation_issues': {
            'patterns': [
                (r'train_test_split.*(?!.*cross_val)', 'Consider using cross-validation for robust evaluation'),
            ],
            'severity': 'suggestion'
        },
        'hyperparameter_tuning': {
            'models_needing_tuning': [
                'RandomForestClassifier', 'RandomForestRegressor', 'GradientBoostingClassifier',
                'GradientBoostingRegressor', 'XGBClassifier', 'XGBRegressor', 'LGBMClassifier',
                'LGBMRegressor', 'SVC', 'SVR', 'MLPClassifier', 'MLPRegressor'
            ],
            'tuning_methods': ['GridSearchCV', 'RandomizedSearchCV', 'HalvingGridSearchCV', 'HalvingRandomSearchCV'],
            'severity': 'suggestion'
        },
        'missing_data_handling': {
            'missing_indicators': [
                r'\.isna\(\)', r'\.isnull\(\)', r'pd\.isna\(', r'pd\.isnull\(', r'np\.isnan\('
            ],
            'imputers': ['SimpleImputer', 'IterativeImputer', 'KNNImputer', 'fillna', 'dropna'],
            'severity': 'warning'
        },
        'model_evaluation': {
            'classification_metrics': [
                'accuracy_score', 'precision_score', 'recall_score', 'f1_score',
                'classification_report', 'confusion_matrix', 'roc_auc_score', 'roc_curve'
            ],
            'regression_metrics': [
                'mean_squared_error', 'mean_absolute_error', 'r2_score',
            ],
            'severity': 'suggestion'
        },
        'code_quality': {
            'patterns': [
                (r'import \*', 'Avoid wildcard imports (import *) - use specific imports'),
                (r'random_state\s*=\s*None', 'Consider setting random_state for reproducibility'),
                (r'print\(.*\)(?!.*logging)', 'Consider using logging instead of print statements'),
            ],
            'severity': 'suggestion'
        },
        'security_performance': {
            'patterns': [
                (r'pd\.read_csv\(.*\)(?!.*nrows)', 'Consider using nrows parameter for large files'),
                (r'\.fit\(.*\)(?!.*n_jobs)', 'Consider using n_jobs=-1 for parallel processing'),
                (r'pickle\.load\(', 'Security risk: pickle.load() can execute arbitrary code'),
                (r'eval\(', 'Security risk: eval() can execute arbitrary code'),
                (r'exec\(', 'Security risk: exec() can execute arbitrary code'),
            ],
            'severity': 'warning'
        },
        'data_preprocessing': {
            'patterns': [
                (r'LabelEncoder\(\)', 'Consider using OneHotEncoder for nominal categorical features in models.'),
                (r'get_dummies\(.*\)(?!.*drop_first)', 'Consider using drop_first=True with get_dummies to avoid multicollinearity.'),
                (r'train_test_split\(.*\)(?!.*stratify)', 'Consider using stratify parameter for classification tasks to maintain class distribution.'),
            ],
            'severity': 'suggestion'
        },
        'model_specific': {
            'tree_based': {
                'models': ['DecisionTreeClassifier', 'DecisionTreeRegressor'],
                'issues': [
                    (r'DecisionTree.*(?!.*max_depth)', 'Consider setting max_depth to prevent overfitting in Decision Trees.'),
                    (r'DecisionTree.*(?!.*min_samples_split)', 'Consider setting min_samples_split to prevent overfitting.'),
                ]
            },
            'ensemble': {
                'models': ['RandomForestClassifier', 'RandomForestRegressor'],
                'issues': [
                    (r'RandomForest.*n_estimators=[1-9]\d?[^0-9]', 'Consider using more estimators (e.g., 100+) in RandomForest for better performance.'),
                ]
            },
            'severity': 'suggestion'
        },
        'good_practices': {
            'patterns': [
                (r'random_state\s*=\s*\d+', 'Good: Using random_state for reproducibility.'),
                (r'Pipeline\(', 'Good: Using sklearn Pipeline for better code organization.'),
                (r'cross_val_score|cross_validate', 'Good: Using cross-validation for robust evaluation.'),
                (r'GridSearchCV|RandomizedSearchCV', 'Good: Using hyperparameter tuning.'),
                (r'StandardScaler|MinMaxScaler|RobustScaler', 'Good: Using feature scaling.'),
                (r'train_test_split\(.*stratify', 'Good: Using stratified sampling.'),
                (r'classification_report|confusion_matrix', 'Good: Using comprehensive evaluation metrics.'),
            ],
            'severity': 'positive'
        }
    }

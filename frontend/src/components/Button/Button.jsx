import { classNames } from '../../helpers/classNames';
import cls from './Button.module.scss';

export const Button = ({
  children, className = '', decoration, ...props
}) => {
  return (
    <button
      type="button"
      className={
        classNames(
          cls.button,
          {},
          [cls[className], decoration === 'black' && cls.decoration, decoration === 'white' && cls.decorationWhite],
        )
      }
      {...props}
    >
      {children}
    </button>
  );
};
